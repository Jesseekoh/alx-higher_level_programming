#!/usr/bin/node

function esrever (list) {
  const n = list.length;
  const reversedList = [];
  for (let i = n - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
}

module.exports = {
  esrever
};
