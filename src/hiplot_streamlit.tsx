import React, { ReactNode } from "react"
import {
  withStreamlitConnection,
  StreamlitComponentBase,
  Streamlit,
} from "./streamlit"
import { HiPlot } from "./hiplot";

import ReactDOM from "react-dom";


interface State {
};

/**
 * This is a React-based component template. It's an alternative to the
 * event-based component pattern. Rather than handling RENDER_EVENT events,
 * you write your rendering logic in the render() function, which is
 * called automatically when appropriate.
 */
class ReactTemplate extends StreamlitComponentBase<State> {
  public render = (): ReactNode => {
    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`. Here, we access the "name" arg.
    const exp = this.props.args["experiment"];
    return (
      <>
        <HiPlot experiment={exp} />
      </>
    )
  }

  // Streamlit.setComponentValue( ... python return value )
}

const componentWrapped = withStreamlitConnection(ReactTemplate)


ReactDOM.render(
  <React.StrictMode>
    {React.createElement(componentWrapped)}
  </React.StrictMode>,
  document.getElementById("root")
)
