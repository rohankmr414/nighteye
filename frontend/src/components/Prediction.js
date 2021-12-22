import React from "react";

import {
  Box,
  Stat,
  StatLabel,
  StatNumber,
  StatHelpText,
  StatArrow,
  StatGroup,
} from "@chakra-ui/react";

export const Prediction = (props) => {
  return (
    <div>
      <Box textAlign={"center"}>
        <Stat>
          <StatLabel>Prediction for tomorrow</StatLabel>
          <StatNumber>{props.pred}</StatNumber>
          {/* <StatHelpText>Feb 12 - Feb 28</StatHelpText> */}
        </Stat>
      </Box>
    </div>
  );
};
