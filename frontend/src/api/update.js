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

export function sendcontent (user_name, content) {
  const data = {
    user_name,
    content
  }
  return request({
    url: '/api/feedback/',
    method: 'post',
    data
  })
}