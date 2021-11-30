pragma solidity ^0.5.3;

contract Helloworld {
  string public greeting;

  function setgreet(string memory _mess) public {
    greeting = _mess;
  }
}
