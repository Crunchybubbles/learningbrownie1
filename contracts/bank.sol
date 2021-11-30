pragma solidity ^0.8.7;

import "OpenZeppelin/openzeppelin-contracts@4.2.0/contracts/token/ERC20/IERC20.sol";


contract Bank {

  mapping(address => uint) public ethBalance;
  mapping(address => IERC20) public tokens;
  mapping(address => mapping(address => uint)) public tokenBalance;


  function depositEth() public payable {
    ethBalance[msg.sender] = msg.value;
  }

  function withdrawEth(uint _outAmount) public {
    require(ethBalance[msg.sender] >= _outAmount);
    ethBalance[msg.sender] -=_outAmount;
    payable(msg.sender).transfer(_outAmount);
  }

  function addToken(address _tokenAddr) public {
    tokens[_tokenAddr] = IERC20(_tokenAddr);
  }

  function depositToken(address _tokenAddr,uint _amount) public {
    tokens[_tokenAddr].transferFrom(msg.sender, address(this), _amount);
    tokenBalance[_tokenAddr][msg.sender] += _amount;
  }

  function withdrawToken(address _tokenAddr, uint _amount) public {
    require(tokenBalance[_tokenAddr][msg.sender] >= _amount);
    tokens[_tokenAddr].approve(msg.sender, _amount);
    tokenBalance[_tokenAddr][msg.sender] -= _amount;
    tokens[_tokenAddr].transfer(msg.sender, _amount);
  }

}
