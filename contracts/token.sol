pragma solidity ^0.8.7;

import "OpenZeppelin/openzeppelin-contracts@4.2.0/contracts/token/ERC20/ERC20.sol";

contract Token1 is ERC20 {

  constructor(uint _supply) ERC20("token1", "TK") {
    _mint(msg.sender, _supply);
  }

}

contract Token2 is ERC20 {

  constructor(uint _supply) ERC20("token2", "TK") {
    _mint(msg.sender, _supply);
  }

}
