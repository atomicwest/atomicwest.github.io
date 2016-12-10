// Jesson Go; December 9, 2016
//ogjdne@gmail.com
//github.com/atomicwest

//------------------------------------------------------
// 1. decimal to other base system
// inval is starting number, sys is the output number system
function fromDecimal(inval, sys){

  // if (! checkBase(inval,sys)) {return 0}

  //force default system
  if (sys<=1 || sys==undefined){ sys = 2 }

  var output = ""
  var nextval = inval
  var digit

  while (nextval!=0){
    digit = nextval%sys
    if (digit > 9) {
      digit = String.fromCharCode(55 + digit)
    }
    output = digit.toString() + output
    nextval = Math.floor(nextval/sys)
  }

  return output

}


//------------------------------------------------------
// 2. other base system to decimal
// orig is the base system of the input inval
function toDecimal(inval, orig){
  // if (! checkBase(inval,orig)) {return 0}
  //force default system
  if (orig<=1 || orig==undefined){ orig = 2 }

  var digits = inval.toString().split("").reverse().join("")
  var total = 0

  for(var i=0; i<digits.length; i++){
    if (digits[i] < 10){
        total += parseInt(digits[i]) * Math.pow(orig,i)
    } else if (typeof(digits[i])=="string"){
        total += digits[i].charCodeAt() * Math.pow(orig,i)
    }
  }

  return total.toString()

}

//------------------------------------------------------
// 3. other base system to other base system
// orig is the starting base, outsys is the output base
function toOther(){

  var inval = parseInt(document.getElementById("convfrom").value)
  var orig = parseInt(document.getElementById("origbase").value)
  var outsys = parseInt(document.getElementById("endbase").value)
  var output

  //force default systems
  if (orig<=1 || orig==undefined){ orig = 2 }
  if (outsys<=1 || outsys==undefined){ outsys = 2 }

  var convert
  if (orig==10){
    output = fromDecimal(inval, outsys)
  } else if (orig<=0) {
    return
  } else {
    convert = parseInt(toDecimal(inval,orig))
    output = fromDecimal(convert,outsys)
  }

  if (inval==0){
      document.getElementById("result").value = "0"
  } else if (! checkBase(inval, orig)) {
      document.getElementById("result").value = "Re-enter input number and/or base"
  } else if (! checkBase(output, outsys)) {
      document.getElementById("result").value = "Re-enter output base"
  } else {
      document.getElementById("result").value = output
  }
}


//------------------------------------------

function hexprefix(){

  var store = document.getElementById("result").value

  if (store.substring(0,2)=="0x"){
    document.getElementById("hex").innerHTML = "Add Hex Prefix"
    document.getElementById("result").value = store.substring(2,store.length)
  } else {
    document.getElementById("hex").innerHTML = "Remove Hex Prefix"
    document.getElementById("result").value = "0x"+store
  }

}

//------------------------------------------
// raises alert and returns False if digits are larger than the base value
function checkBase(number, base){
  var strArr = number.toString().split("")
  for (var i=0; i<strArr.length; i++) {
    if (parseInt(strArr[i]) >= base) {
      alert("One or more digits are larger than the base value.\nPlease enter a valid input/base combination")
      console.log(number)
      console.log(base)
      return false
    }
  }
  return true
}

//------------------------------------------
function clearfield(){
  document.getElementById("convfrom").value = 0
  document.getElementById("origbase").value = 2
  document.getElementById("endbase").value = 2
  document.getElementById("result").value = 0
}
