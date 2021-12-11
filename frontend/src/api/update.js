import request from '@/utils/request'

export function updatepassword (username, password) {
  const data = {
    username,
    password
  }
  return request({
    url: '/api/update_password/',
    method: 'post',
    data
  })
}

export function sendcontent (username, content, gentime) {
  const data = {
    username,
    content,
    gentime
  }
  return request({
    url: '/api/feedback/',
    method: 'post',
    data
  })
}
