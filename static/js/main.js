/**
 * Updates the current color, distance and motor status calling teh corresponding methods
 */
function updateStatus() {
  // Update current color based on Open CV
  updateCurrentColorOpenCV()
  
  // Update motor status
  updateMotorStatus()
  
  // Update current color based on distance
  updateDistance()

  // Update current distance
  //updateCurrentColorDistance()
}

/**
 * Update the current color based on OpenCV
 */
 async function updateCurrentColorOpenCV() {
  try {
    // Request color from server
    const requestResult = await requestColorFromOpenCV()
    // Get the HTML element where the status is displayed
    const green_open_cv = document.getElementById('green_open_cv')
    green_open_cv.innerHTML = requestResult.data[0]
    const purple_open_cv = document.getElementById('purple_open_cv')
    purple_open_cv.innerHTML = requestResult.data[1]
    const yellow_open_cv = document.getElementById('yellow_open_cv')
    yellow_open_cv.innerHTML = requestResult.data[2]
  } catch (e) {
    console.log('Error getting the color based on OpenCV', e)
    //updateStatus('Error getting the color based on OpenCV')
  }
}

/**
 * Function to request the server to update the current color based on OpenCV
 */
 function requestColorFromOpenCV () {
  try {
    // Make request to server
    return axios.get('/get_color_from_opencv')
  } catch (e) {
    console.log('Error getting the status', e)
    //updateStatus('Error getting the status')
  }
}


/**
 * Function to request the server to start the motor
 */
 function requestStartMotor () {
  //...
  try {
    return axios.get('/start_motor')
  } catch (e) {
    console.log('Error starting the motor', e)
    //updateStatus('Error starting the motor')
  }
}


/**
 * Function to request the server to stop the motor
 */
function requestStopMotor () {
  //...
  try {
    return axios.get('/stop_motor')
  } catch (e) {
    console.log('Error stopping the motor', e)
    //updateStatus('Error stopping the motor')
  }
}

/**
 * Update the status of the motor
 * @param {String} status 
 */
 async function updateMotorStatus(status) {
  // Get the HTML element where the status is displayed
  try {//return
    const requestResult = await axios.get('/motor_status')
    const status = document.getElementById('motor_status')
    status.innerHTML = requestResult.data
  } catch (e) {
    console.log('Error showing motor status', e)
    //updateStatus('Error showing motor status')
  }

}

/**
 * Update the current color based on distance sensor
 */
 async function updateDistance() {
  // Get the HTML element where the status is displayed
  // ...
  try {
    var requestResult = await requestDistance()
    var distance = document.getElementById('distance_status')
    distance.innerHTML = requestResult.data
  } catch (e) {
    console.log('Error showing current color based on distance status', e)
  }
  updateCurrentColorDistance()
}


/**
 * Function to request the server to get the distance from
 * the rod to the ultrasonic sensor
 */
function requestDistance () {
  //...
  try {
    return axios.get('/get_distance')
  } catch (e) {
    console.log('Error getting the distance', e)
  }
}


/**
 * Update the current color based on distance sensor
 */
 async function updateCurrentColorDistance() {
  // Get the HTML element where the status is displayed
  // ...
  try {
    // Request color from server
    const requestResult = await requestColorFromDistance()
    // Get the HTML element where the status is displayed
    const green_from_distance = document.getElementById('green_from_distance')
    green_from_distance.innerHTML = requestResult.data[0]
    const purple_from_distance = document.getElementById('purple_from_distance')
    purple_from_distance.innerHTML = requestResult.data[1]
    const yellow_from_distance = document.getElementById('yellow_from_distance')
    yellow_from_distance.innerHTML = requestResult.data[2]
  } catch (e) {
    console.log('Error getting the color based on distance', e)
  }
}


/**
 * Function to request the server to get the color based
 * on distance only
 */
function requestColorFromDistance () {
  //...
  try {
    return axios.get('/get_color_from_distance')
  } catch (e) {
    console.log('Error getting the color using distance', e)
  }
}
