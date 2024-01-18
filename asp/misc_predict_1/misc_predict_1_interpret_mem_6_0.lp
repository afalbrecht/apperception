% misc_predict_1

% Permanents

% Rules
rule_body(r1,s(c_on,var_sensor_1_1)).
rule_head_causes(r1,s(c_off,var_sensor_1_1)).

rule_body(r2,s(c_off,var_sensor_1_1)).
rule_head_causes(r2,s(c_on,var_sensor_1_1)).

