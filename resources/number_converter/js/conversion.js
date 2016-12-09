// 1. decimal to other base system
// 2. other base system to decimal
// 3. other base system to other base system

var input = 23
var base = 10

//------------------------------------------------------
// 1. decimal to other base system
// inval is starting number, sys is the output number system
function fromdecimal(inval, sys){
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

console.log(fromdecimal(29,2))
console.log(fromdecimal(29,16))
console.log(fromdecimal(290,16))
console.log(fromdecimal(31315,15))
console.log(fromdecimal(10710049,16))

//------------------------------------------------------
// 2. other base system to decimal
// orig is the base system of the input inval
function todecimal(inval, orig){

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

console.log(todecimal(11101,2))

//------------------------------------------------------
// 3. other base system to other base system
// orig is the starting base, outsys is the output base
function toother(inval, orig, outsys){

  //force default systems
  if (orig<=1 || orig==undefined){ orig = 2 }
  if (outsys<=1 || outsys==undefined){ outsys = 2 }

  var convert
  if (orig==10){
    return fromdecimal(inval, outsys)
  } else if (orig<=0) {
    return
  } else {
    convert = parseInt(todecimal(inval,orig))
    return fromdecimal(convert,outsys)
  }
}

console.log(toother(25,8,2))
console.log(toother(101110101,2,16))
