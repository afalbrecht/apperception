% sokoban_predict_e3

% Permanents
permanent(isa(p_is_not_wall,obj_cell_1_1)).
permanent(isa2(p_below,obj_cell_1_1,obj_cell_1_2)).
permanent(isa(p_is_not_wall,obj_cell_1_2)).
permanent(isa2(p_below,obj_cell_1_2,obj_cell_1_3)).
permanent(isa(p_is_not_wall,obj_cell_1_3)).
permanent(isa2(p_below,obj_cell_1_3,obj_cell_1_4)).
permanent(isa(p_is_not_wall,obj_cell_1_4)).

% Rules
rule_body(r1,isa2(p_below,var_cell_1,var_cell_2)).
rule_body(r1,s(c_south,var_player_1)).
rule_body(r1,s2(c_in_1,var_player_1,var_cell_1)).
rule_head_causes(r1,s2(c_in_1,var_player_1,var_cell_2)).

rule_body(r2,isa2(p_below,var_cell_1,var_cell_2)).
rule_body(r2,s(c_north,var_player_1)).
rule_body(r2,s2(c_in_1,var_player_1,var_cell_2)).
rule_head_causes(r2,s2(c_in_1,var_player_1,var_cell_1)).

