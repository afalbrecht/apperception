% sokoban_predict_e3


% Rules
rule_body(r1,isa2(p_below,var_cell_1,var_cell_2)).
rule_body(r1,s(c_south,var_1_1)).
rule_body(r1,s2(c_in_1,var_1_1,var_cell_1)).
rule_head_causes(r1,s2(c_in_1,var_1_1,var_cell_2)).

rule_body(r2,isa2(p_below,var_cell_1,var_cell_2)).
rule_body(r2,s(c_north,var_1_1)).
rule_body(r2,s2(c_in_1,var_1_1,var_cell_2)).
rule_head_causes(r2,s2(c_in_1,var_1_1,var_cell_1)).

