% sokoban_predict_e0

% Permanents
permanent(isa(p_is_not_wall,obj_cell_1_1)).
permanent(isa2(p_right,obj_cell_1_1,obj_cell_2_1)).
permanent(isa(p_is_not_wall,obj_cell_2_1)).
permanent(isa2(p_right,obj_cell_2_1,obj_cell_3_1)).
permanent(isa(p_is_not_wall,obj_cell_3_1)).
permanent(isa2(p_right,obj_cell_3_1,obj_cell_4_1)).
permanent(isa(p_is_not_wall,obj_cell_4_1)).
permanent(isa2(p_right,obj_cell_4_1,obj_cell_5_1)).
permanent(isa(p_is_not_wall,obj_cell_5_1)).
permanent(isa2(p_right,obj_cell_5_1,obj_cell_6_1)).
permanent(isa(p_is_not_wall,obj_cell_6_1)).
permanent(isa2(p_right,obj_cell_6_1,obj_cell_7_1)).
permanent(isa(p_is_not_wall,obj_cell_7_1)).
permanent(isa2(p_right,obj_cell_7_1,obj_cell_8_1)).
permanent(isa(p_is_not_wall,obj_cell_8_1)).

% Rules
rule_body(r1,isa(p_is_not_wall,var_cell_1)).
rule_body(r1,isa2(p_right,var_cell_2,var_cell_1)).
rule_body(r1,s(c_east,var_1_1)).
rule_body(r1,s2(c_in_1,var_1_1,var_cell_2)).
rule_head_causes(r1,s2(c_in_1,var_1_1,var_cell_1)).

