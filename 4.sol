// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

contract Student {

    struct StudentData 
    {
        uint rollno;
        string name;
        uint marks;
    }

    StudentData[] public students;

    function addStudent(uint r, string memory n, uint m) public {
        students.push(StudentData(r,n,m));
    }

    function getStudent(uint i) public view returns(uint,string memory,uint) {
        return(students[i].rollno, students[i].name, students[i].marks);
    }

    receive() external payable {

    }

    fallback() external payable {
    }
}