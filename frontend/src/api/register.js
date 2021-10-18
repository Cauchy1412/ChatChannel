import request from '@/utils/request'

export function registerByUsername (username, password) {
  const data = {
    username,
    password
  }
  return request({
    url: '/api/register/',
    method: 'post',
    data
  })
}
