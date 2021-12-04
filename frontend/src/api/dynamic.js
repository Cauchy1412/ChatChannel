import request from '@/utils/request'

export function addDynamic (data) {
  return request({
    url: '/api/add_dynamic/',
    method: 'post',
    data
  })
}

export function getHistoryDynamic () {
  return request({
    url: '/api/history_dynamic/',
    method: 'post'
  })
}