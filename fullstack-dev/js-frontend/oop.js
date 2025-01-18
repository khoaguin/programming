class Person {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    fullName() {
        return `${this.firstName} ${this.lastName}`;
    }
}

const myPerson = new Person("John", "Smith");
console.log(myPerson.fullName());  // outputs "John Smith"