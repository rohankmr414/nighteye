import React from "react";
import { Container } from "@chakra-ui/react";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

import { Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export const options = {
  responsive: true,
  plugins: {
    legend: {
      position: "top",
    },
    title: {
      display: true,
      text: "Past 15 Days",
    },
  },
};

const getDates = () => {
  let dates = [];
  for (let i = 0; i < 15; i++) {
    let date = new Date();
    date.setDate(date.getDate() - i);
    dates.push(date.getDate());
  }
  dates.reverse();
  return dates;
};

const labels = getDates();

const Linechart = (props) => {
  return (
    <div>
      <Container maxW="container.md">
        <Line
          options={options}
          data={{
            labels,
            datasets: [
              {
                label: props.label,
                data: props.data,
                borderColor: "rgb(255, 99, 132)",
                backgroundColor: "rgba(255, 99, 132, 0.5)",
              },
            ],
          }}
        />
      </Container>
    </div>
  );
};

export default Linechart;
