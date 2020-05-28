# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import warnings
from pathlib import Path
import typing as tp
from .experiment import ExperimentDisplayed, Experiment, Datapoint


class HiPlotStreamlitRegisterError(Exception):
    pass


def register_streamlit() -> None:
    import streamlit as st
    if not hasattr(st, 'declare_component'):
        raise HiPlotStreamlitRegisterError('Incompatible streamlit version')
    if not st._is_running_with_streamlit:
        return

    built_path = (Path(__file__).parent / "static" / "built" / "streamlit_component").resolve()
    assert (built_path / "index.html").is_file(), f"""HiPlot component does not appear to exist in {built_path}
If you did not install hiplot using official channels (pip, conda...), maybe you forgot to build javascript files?
See https://facebookresearch.github.io/hiplot/contributing.html#building-javascript-bundle
"""
    HiPlotComponent = st.declare_component(path=str(built_path))

    def create_instance_wrapper(f: tp.Any, exp: Experiment, key: tp.Optional[str] = None) -> tp.Any:
        if key is None:
            warnings.warn(f"""Creating a HiPlot component with key=None will make refreshes slower.
Please use `st.hiplot(..., key=\"some_unique_key\")`""")
        return f(experiment=exp._asdict(), key=key)
    HiPlotComponent(create_instance_wrapper)

    st.register_component("hiplot", HiPlotComponent)
