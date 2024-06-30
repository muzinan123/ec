<template>
  <div class="app-container">
    <node-card :data="nodeInfo" />
    <application-card :apps="apps" />
    <device-card :devices="devices" />
    <node-usage-card :metrics="metrics" />
    <labels-card :labels="labels" />
  </div>
</template>
<script>
  import NodeCard from '@/components/Card/NodeCard'
  import NodeUsageCard from '@/components/Card/NodeUsageCard'
  import LabelsCard from '@/components/Card/LabelsCard'
  import ApplicationCard from '@/components/Card/ApplicationCard'
  import DeviceCard from '@/components/Card/DeviceCard'
  //单位与数值的对应关系
  const UNIT_MAP = {
    'Mi': 1024 * 1024,
    'Ki': 1024
  }

  export default {
    name: 'Detail',
    components: { NodeCard, NodeUsageCard, LabelsCard, ApplicationCard, DeviceCard },
    data() {
      return {
        nodeInfo: {
          'title': null,
          'content': null
        },
        labels: null,
        tempRoute: {},
        //资源使用情况
        metrics: {
          cpu: {
            allocatable: 0, usage: 0
          },
          memory: {
            allocatable: 0, usage: 0
          }
        },
        //设备信息
        devices: [],
        //应用信息
        apps: []
      }
    },
    created() {
      this.tempRoute = Object.assign({}, this.$route)
      this.getNodeItem()
      this.getNodeMetrics()
      this.getNodeDevice()
      this.getNodeApp()
      this.setPageTitle()
      this.setTagsViewTitle()
    },
    methods: {
      getNodeItem() {
        this.$store.dispatch('edge-node/getNodeItem', this.$route.params.id)
          .then(response => {
            //获取数据返回的节点信息字段
            let nodeinfo = response.status.node_info
            this.nodeInfo = {
              title: '节点信息',
              content: {
                name: response.metadata.name,
                architecture: nodeinfo.architecture,
                container_runtime_version: nodeinfo.container_runtime_version,
                kernel_version: nodeinfo.kernel_version,
                kube_proxy_version: nodeinfo.kube_proxy_version,
                kubelet_version: nodeinfo.kubelet_version,
                operating_system: nodeinfo.operating_system,
                os_image: nodeinfo.os_image
              }
            }
            this.labels = response.metadata.labels
            //从节点信息中获取资源节点资源总量
            let allocatable = response.status.allocatable
            this.metrics.cpu.allocatable = parseInt(allocatable.cpu * Math.pow(10, 9))
            let lent = allocatable.memory.length
            //单位
            let unit = (allocatable.memory).substring(lent - 2, lent)
            this.metrics.memory.allocatable = parseInt(allocatable.memory) * UNIT_MAP[unit]
          })
      },
      getNodeMetrics() {
        this.$store.dispatch('metrics/getNodeMetrics', this.$route.params.id)
          .then(response => {
            const usage = response.usage
            let lent = usage.memory.length
            //单位
            let unit = (usage.memory).substring(lent - 2, lent)
            //计算使用的CPU和内存
            this.metrics.cpu.usage = parseInt(usage.cpu)
            this.metrics.memory.usage = parseInt(usage.memory) * UNIT_MAP[unit]
          })

      },
      //节点绑定设备信息
      getNodeDevice() {
        const currentNode = this.$route.params.id
        this.$store.dispatch('edge-device/getDeviceList')
          .then(response => {
            let result = []
            //获取设备数据，按照节点名称过滤
            response.forEach((item, index) => {
              let nodeNameList = item.spec.nodeSelector.nodeSelectorTerms[0].matchExpressions[0].values
              if (nodeNameList.indexOf(currentNode) === -1) {
                return
              }
              result.push(
                {
                  name: item.metadata.name,
                  createTime: item.metadata.creationTimestamp
                }
              )
            })
            this.devices = result
          })
      },
      //节点应用信息
      getNodeApp() {
        const currentNode = this.$route.params.id
        this.$store.dispatch('edge-app/getAppList').then(response => {
          let result = []
          response.forEach((item, index) => {
            let eachNode = item.spec.node_name
            if (eachNode !== currentNode) {
              return
            }
            let images = []
            //计算镜像
            item.spec.containers.forEach((item_c, index_c) => {
              images.push(
                item_c.image
              )
            })
            result.push({
              name: item.metadata.name,
              createTime: item.metadata.creation_timestamp,
              labels: item.metadata.labels,
              images: images,
              node: item.spec.node_name,
              status: item.status.phase === 'Running' ? 0 : 1
            })
          })
          this.apps = result
        })
      },
      setPageTitle() {
        const title = '节点详情'
        document.title = `${title} - ${this.$route.params.id}`
      },
      setTagsViewTitle() {
        const title = '节点详情'
        const route = Object.assign({}, this.tempRoute, { title: `${title}-${this.$route.params.id}` })
        this.$store.dispatch('tagsView/updateVisitedView', route)
      }
    }
  }
</script>
<style scoped>
  .app-container > * {
    margin: 20px 0;
  }
</style>
