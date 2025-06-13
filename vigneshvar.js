// const person={
//   firstname:"Sita ",
//   lastname:"Ram",
//    get fullname(){
//    return this.firstname+" "+this.lastname;
//   },
//   set fullname(name){
//     const parts=name.split(" ");
//     this.firstname=parts[0];
//     this.lastname=parts[1];
//   }
// };
// console.log(person);
// console.log(person.fullname);
// person.fullname="shankar";
// console.log(person.fullname);

class person {
  constructor(firstname,lastname){
    this.firstname=firstname;
    this.lastname=lastname;

  }
  get fullname(){
    return this.firstname +" "+this.lastname;
  }

};
const p1=new person("muthu","kumar");
console.log(p1);
console.log(p1.fullname);

class circle{
  constructor(radius){
    this.radius=radius;
  }
  get diameter(){
    return this.radius*2;
  }
  set diameter(diameter){
    this.radius=diameter/2;
  }
  get area(){
  return  Math.PI*this.radius*this.radius;
  }
};
const mycircle=new circle(5);
console.log(mycircle.area);
console.log(mycircle.diameter);
console.log(mycircle.radius);


class myclass{
  static hoo="ganapathy";
  static mystaticmethod(){
    console.log("Hello ")
  }
};
myclass.mystaticmethod();
console.log(myclass.hoo);
class mathu{
  static add(a,b){
    return a+b;
  }
};
console.log(mathu.add(12,23));