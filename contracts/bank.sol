pragma solidity ^0.8.4;

contract Bank {

  mapping(address => uint) bankaccount;

  function deposit() public payable {
    bankaccount[msg.sender] = msg.value;
  }

  function withdraw() public payable {
    uint outamount = msg.value;
    uint amount = bankaccount[msg.sender];
    require(outamount <= amount);
    payable(msg.sender).transfer(outamount);

  }

}
