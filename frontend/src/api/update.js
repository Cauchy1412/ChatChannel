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

export function sendcontent (username, content, gen_time) {
  const data = {
    username,
    content,
    gen_time
  }
  return request({
    url: '/api/feedback/',
    method: 'post',
    data
  })
}
