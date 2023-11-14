#!/usr/bin/node

const callMeMoby = (a, functionToExecute) => {
  for (let i = 0; i < a; i++) functionToExecute();
};

module.exports = {
  callMeMoby
};
