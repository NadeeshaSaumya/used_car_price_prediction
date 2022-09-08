function getSeatsValue() {
  var uiSEATS = document.getElementsByName("uiSEATS");
  for(var i in uiSEATS) {
    if(uiSEATS[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getTransmissionValue() {
  var uiTransmission = document.getElementsByName("uiTransmission");
  for(var i in uiTransmission) {
    if(uiTransmission[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getFuel_typeValue() {
  var uiFuel_type = document.getElementsByName("uiFuel_type");
  for(var i in uiFuel_type) {
    if(uiFuel_type[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getOwner_typeValue() {
  var uiOwner_type = document.getElementsByName("uiOwner_type");
  for(var i in uiOwner_type) {
    if(uiOwner_type[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var Power = document.getElementById("uiPOWER");
  var Mileage = document.getElementById("uiMileage");
  var Engine = document.getElementById("uiEngine");
  var Kilometer_Drive = document.getElementById("uiDrivekm");
  var Year = document.getElementById("uiYear");
  var Seats = getSeatsValue();
  var Transmission = getTransmissionValue();
  var Fuel_type = getFuel_typeValue();
  var Owner_type = getOwner_typeValue();
  var Name = document.getElementById("uiNames");
  var estPrice = document.getElementById("uiEstimatedPrice");

  // var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      total_sqft: parseFloat(sqft.value),
      bhk: bhk,
      bath: bathrooms,
      location: location.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;