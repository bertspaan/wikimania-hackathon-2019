const request = require('request')

request.post('https://commons.wikimedia.org/wiki/Special:Export', {
  form: {
    pages: 'Data:Ncei.noaa.gov/weather/New_York_City.tab',
    curonly: 1
  }
}, (error, res, body) => {
  if (error) {
    console.error(error)
    return
  }
  var json = body.match(/<text.*?>(.*)<\/text>/)
  json = JSON.parse(json[1])

  console.log(json)
})