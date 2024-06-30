import request from '@/utils/request'

export function fetchList() {
  return request({
    url: '/pod/pod/default/',
    method: 'get'
  })
}

export function fetchItem(name) {
  return request({
    url: '/pod/pod/default/' + name + '/',
    method: 'get'
  })
}

export function create(data) {
  return request({
    url: '/pod/pod/',
    method: 'post',
    data
  })
}

//删除应用
export function deleteApp(data) {
  return request({
    url: '/pod/pod/',
    method: 'delete',
    data
  })
}
