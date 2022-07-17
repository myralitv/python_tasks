def ice_cream(ice_cream_ball: int) -> str:
    if not isinstance(ice_cream_ball, int):
        raise TypeError(f'Argument "ice_cream_ball" must be integer, not {type(ice_cream_ball)}')
    if ice_cream_ball < 0:
        raise ValueError(f'Argument "ice_cream_ball":{ice_cream_ball} must be greater than 0')

    ice_cream_var1 = 3
    ice_cream_var2 = 5
    if ice_cream_ball == ice_cream_var1 or ice_cream_ball == ice_cream_var2 \
            or ice_cream_ball == (ice_cream_var1 + ice_cream_var2):
        return "Yes"
    else:
        return "No"
