import request from '@/utils/request'

export function getwithdrawMessages () {
  return request({
    url: '/api/get_withdrawMessages/',
    method: 'get'
  })
}

export function getfeedbacks () {
  return request({
    url: '/api/get_feedbacks/',
    method: 'get'
  })
}
