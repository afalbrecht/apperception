% sokoban_predict_e4

% Permanents
permanent(isa(p_is_not_wall,obj_cell_1_1)).
permanent(isa2(p_below,obj_cell_1_1,obj_cell_1_2)).
permanent(isa2(p_right,obj_cell_1_1,obj_cell_2_1)).
permanent(isa(p_is_not_wall,obj_cell_1_2)).
permanent(isa2(p_below,obj_cell_1_2,obj_cell_1_3)).
permanent(isa2(p_right,obj_cell_1_2,obj_cell_2_2)).
permanent(isa(p_is_not_wall,obj_cell_1_3)).
permanent(isa2(p_right,obj_cell_1_3,obj_cell_2_3)).
permanent(isa(p_is_not_wall,obj_cell_2_1)).
permanent(isa2(p_below,obj_cell_2_1,obj_cell_2_2)).
permanent(isa2(p_right,obj_cell_2_1,obj_cell_3_1)).
permanent(isa(p_is_not_wall,obj_cell_2_2)).
permanent(isa2(p_below,obj_cell_2_2,obj_cell_2_3)).
permanent(isa2(p_right,obj_cell_2_2,obj_cell_3_2)).
permanent(isa(p_is_not_wall,obj_cell_2_3)).
permanent(isa2(p_right,obj_cell_2_3,obj_cell_3_3)).
permanent(isa(p_is_not_wall,obj_cell_3_1)).
permanent(isa2(p_below,obj_cell_3_1,obj_cell_3_2)).
permanent(isa2(p_right,obj_cell_3_1,obj_cell_4_1)).
permanent(isa(p_is_not_wall,obj_cell_3_2)).
permanent(isa2(p_below,obj_cell_3_2,obj_cell_3_3)).
permanent(isa2(p_right,obj_cell_3_2,obj_cell_4_2)).
permanent(isa(p_is_not_wall,obj_cell_3_3)).
permanent(isa2(p_right,obj_cell_3_3,obj_cell_4_3)).
permanent(isa(p_is_not_wall,obj_cell_4_1)).
permanent(isa2(p_below,obj_cell_4_1,obj_cell_4_2)).
permanent(isa(p_is_not_wall,obj_cell_4_2)).
permanent(isa2(p_below,obj_cell_4_2,obj_cell_4_3)).
permanent(isa(p_is_not_wall,obj_cell_4_3)).
