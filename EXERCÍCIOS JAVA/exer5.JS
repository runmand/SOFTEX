var numbers = [1,2,3,4,5,6,7,8,9,10];
var sum = numbers.reduce(function(accumulator,value){
  return accumulator + value
},0);

console.log(sum);