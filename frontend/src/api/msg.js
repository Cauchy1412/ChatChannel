import request from '@/utils/request'

export function getHistoryMsg () {
  return request({
    url: '/api/history_msg/',
    method: 'get'
  })
}

export function addHistoryMsg (data) {
  return request({
    url: '/api/history_msg/',
    method: 'post',
    data
  })
}

export function delHistoryMsg (data) {
  return request({
    url: '/api/delete_msg/',
    method: 'post',
    data
  })
}
