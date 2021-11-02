import request from '@/utils/request'

export function createChatRoom (data) {
  return request({
    url: '/api/add_chat_room/',
    method: 'post',
    data
  })
}

export function joinChatRoom (data) {
    return request({
      url: '/api/join_chat_room/',
      method: 'post',
      data
    })
  }
