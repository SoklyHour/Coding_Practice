const { width } = require("@mui/system");

const car = {
    color: "red",
    type: "toyota",
    model: "2024"
}
console.log(car.color);

const person = {
    firstName: "John",
    lastName: "Doe",
    age : "30",
    getFullName() {
        return `${this.firstName} ${this.lastName}`;
      }
    
}

person.age = 25;
console.log(person.age)


car.color = "red";
console.log(car); 

const student = {
    name: "Jane",
    age: 20,
    address: {
        street: "123 Main St",
        city:"Anytown",
        state: "CA",
    }
}
console.log(student)

const rectangle = {
    length: 10,
    width: 5,
  
    getArea() {
      return this.length * this.width;
    }
  };
  
  console.log(rectangle.getArea());