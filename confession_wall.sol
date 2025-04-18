// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ConfessionWall {
    struct Confession {
        uint id;
        string message;
        address owner;
        uint timestamp;
    }

    uint public confessionCount;
    mapping(uint => Confession) public confessions;

    event NewConfession(uint id, string message, address owner, uint timestamp);

    constructor() {
        confessionCount = 0;
    }

    function confess(string memory _message) public {
        confessionCount++;
        confessions[confessionCount] = Confession(confessionCount, _message, msg.sender, block.timestamp);
        emit NewConfession(confessionCount, _message, msg.sender, block.timestamp);
    }

    function getConfession(uint _id) public view returns (string memory, address, uint) {
        Confession memory confession = confessions[_id];
        return (confession.message, confession.owner, confession.timestamp);
    }
}
