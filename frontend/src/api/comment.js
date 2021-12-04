import request from '@/utils/request'

export function addcomment (data) {
  return request({
    url: '/api/add_comment/',
    method: 'post',
    data
  })
}

export function getcomment () {
    return request({
      url: '/api/get_comment/',
      method: 'get',
      data
    })
}