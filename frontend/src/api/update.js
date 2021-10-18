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
