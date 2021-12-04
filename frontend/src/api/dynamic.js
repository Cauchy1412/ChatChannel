import request from '@/utils/request'

export function adddynamic (data) {
  return request({
    url: '/api/add_dynamic/',
    method: 'post',
    data
  })
}

export function getHistoryDynamic () {
  return request({
    url: '/api/get_dynamics/',
    method: 'get'
  })
}
