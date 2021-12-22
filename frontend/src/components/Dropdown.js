import React from "react";
import {
  Box,
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
  Image,
  Button,
} from "@chakra-ui/react";

import { ChevronDownIcon } from "@chakra-ui/icons";

const Dropdown = (props) => {
  return (
    <div>
      <Box textAlign={"center"}>
        <Menu>
          <MenuButton as={Button} rightIcon={<ChevronDownIcon />}>
            Coin List
          </MenuButton>
          <MenuList>
            <MenuItem minH="40px" onClick={() => props.clickMe("bitcoin")}>
              <Image
                boxSize="2rem"
                borderRadius="full"
                src="https://cryptologos.cc/logos/bitcoin-btc-logo.svg?v=014"
                alt="BTC"
                mr="12px"
              />
              <span>Bitcoin</span>
            </MenuItem>
            <MenuItem minH="40px" onClick={() => props.clickMe("ethereum")}>
              <Image
                boxSize="2rem"
                borderRadius="full"
                src="https://cryptologos.cc/logos/ethereum-eth-logo.svg?v=014"
                alt="ETH"
                mr="12px"
              />
              <span>Ethereum</span>
            </MenuItem>
            <MenuItem minH="40px" onClick={() => props.clickMe("solana")}>
              <Image
                boxSize="2rem"
                borderRadius="full"
                src="https://cryptologos.cc/logos/solana-sol-logo.svg?v=014"
                alt="SOL"
                mr="12px"
              />
              <span>Solana</span>
            </MenuItem>
            <MenuItem minH="40px" onClick={() => props.clickMe("cardano")}>
              <Image
                boxSize="2rem"
                borderRadius="full"
                src="https://cryptologos.cc/logos/cardano-ada-logo.svg?v=014"
                alt="ADA"
                mr="12px"
              />
              <span>Cardano</span>
            </MenuItem>
            <MenuItem minH="40px" onClick={() => props.clickMe("polygon")}>
              <Image
                boxSize="2rem"
                borderRadius="full"
                src="https://cryptologos.cc/logos/polygon-matic-logo.svg?v=014"
                alt="MATIC"
                mr="12px"
              />
              <span>Polygon</span>
            </MenuItem>
          </MenuList>
        </Menu>
      </Box>
    </div>
  );
};

export default Dropdown;
