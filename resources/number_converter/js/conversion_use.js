// Jesson Go; December 9, 2016
//ogjdne@gmail.com
//github.com/atomicwest

//------------------------------------------------------
// 1. decimal to other base system
// inval is starting number, sys is the output number system
function fromDecimal(inval, sys){
  //force default system
  if (sys<=1 || sys==undefined){ sys = 2 }

  var output = ""
  var nextval = parseInt(inval)
  var digit

  while (nextval!=0){
    digit = nextval%sys
    if (digit > 9) {
      digit = String.fromCharCode(55 + digit)
    }
    output = digit.toString() + output
    nextval = Math.floor(nextval/sys)
  }
  if (inval=="0") {output = "0"}
  return output

}

//------------------------------------------------------
// 2. other base system to decimal
// orig is the base system of the input inval
function toDecimal(inval, orig){

  var numalpha = numalph();
  var inputvalue = inval.toString();
  var digits = inputvalue.toUpperCase().split("").reverse().join("");
  var total = 0;

  for(var i=0; i<digits.length; i++){
    total += numalpha[digits[i]] * Math.pow(orig,i)
  }

  return total.toString()

}

//------------------------------------------------------
// 3. other base system to other base system
// orig is the starting base, outsys is the output base
function toOther(){

  var inval = document.getElementById("convfrom").value.toUpperCase();
  var orig = document.getElementById("origbase").value.toUpperCase();
  var outsys = document.getElementById("endbase").value.toUpperCase();

  if (! isNum(orig)) {
    alert('Original radix contains letters or is blank')
    document.getElementById("origbase").focus();
    return
  } else if (! isNum(outsys)) {
    alert('Final radix contains letters or is blank')
    document.getElementById("endbase").focus();
    return
  }

  var output;

  var convert;
  if (orig==10){
    output = fromDecimal(inval, outsys);
  } else {
    convert = toDecimal(inval,orig);
    output = fromDecimal(convert,outsys);
  }

  if (inval=="0"){
      document.getElementById("result").value = "0";
  } else if (! checkBase(inval, orig)) {
      document.getElementById("result").value = "Re-enter input and/or base";
  } else if (! checkBase(output, outsys)) {
      document.getElementById("result").value = "Re-enter output base";
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
// raises alert and returns False if input digits are larger than the base value
function checkBase(number, base){
  var numalpha = numalph()
  var thisnum = number.toString()
  var strArr = thisnum.toUpperCase().split("")
  for (var i=0; i<strArr.length; i++) {
    if ((numalpha[strArr[i]] >= base) || numalpha[strArr[i]]==null) {
      alert("One or more digits are larger than the base value.\nPlease enter a valid input/base combination")
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

//------------------------------------------
function isNum(value) {
  var nums = ["0","1","2","3","4","5","6","7","8","9"]
  var splitval = value.split("")
  var check = true
  if (value.length==0) { check = false }
  splitval.forEach(function(item) {
      // debugger
      if ($.inArray(item,nums)===-1) { check = false }
  })
  return check
}

//------------------------------------------
function numalph() {
  var obj={};
  for (var j=0; j<10; j++){
    obj[j.toString()] = j
  }
  for (var v=10; v<16; v++) {
    obj[String.fromCharCode(v+55)] = v
  }
  return obj
}
