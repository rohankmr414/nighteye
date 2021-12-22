import Navbar from "./components/Navbar";
import Dropdown from "./components/Dropdown";
import Linechart from "./components/Linechart";
import { Prediction } from "./components/Prediction";
import React from "react";
import Axios from "axios";

const getPrediction = async (coin, prices) => {
  let pred = await Axios.post(
    `http://127.0.0.1:8000/predict/`,
    {
      baseID: coin,
      values: prices,
    },
    {
      headers: {
        Authorization: ``,
        "Content-Type": "application/json",
      },
    }
  );
  console.log(pred.data);
  return String(pred.data.prediction.toFixed(2));
};

const getData = async (coin) => {
  let end = new Date().getTime();
  let start = end - 86400000 * 15;
  let url = `http://127.0.0.1:8000/prices/?start=${start}&end=${end}&baseID=${coin}`;
  let res = await Axios.get(url);

  let pred = await getPrediction(coin, res.data.prices);
  return { prices: res.data.prices, prediction: pred };
};

const getDates = () => {
  let dates = [];
  for (let i = 0; i < 15; i++) {
    let date = new Date();
    date.setDate(date.getDate() - i);
    dates.push(date.getDate());
  }
  return dates;
};

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      labels: [],
      label: "",
      data: [],
      pred: "",
    };
    console.log(this.state);
  }

  handleClick = (coin) => {
    getData(coin).then((data) => {
      this.setState(
        {
          labels: getDates(),
          label: coin,
          data: data.prices,
          pred: `$${data.prediction}`,
        },
        () => console.log(this.state)
      );
    });
  };
  render() {
    return (
      <div className="App">
        <Navbar />
        <br></br>
        <Dropdown clickMe={this.handleClick} />
        <br></br>
        <br></br>
        <Linechart
          labels={this.state.lables}
          label={this.state.label}
          data={this.state.data}
        />
        <br></br>
        <br></br>
        <Prediction pred={this.state.pred} />
      </div>
    );
  }
}

export default App;
