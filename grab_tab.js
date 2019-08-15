const request = require('request')

request.post('https://commons.wikimedia.org/wiki/Special:Export', {
  form: {
    pages: 'Data:Ncei.noaa.gov/weather/New_York_City.tab'
  }
}, (error, res, body) => {
  if (error) {
    console.error(error)
    return
  }
  console.log(`statusCode: ${res.statusCode}`)
  console.log(body)
})