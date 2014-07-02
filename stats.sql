select cs_tdf_gc.name,cs_tdf_gc.points as 'TDF GC',cs_tdf_mountains.points as Mountain ,cs_tdf_points.points as Points
from cs_tdf_gc inner join cs_tdf_mountains on cs_tdf_gc.name = cs_tdf_mountains.name 
	inner join cs_tdf_points on cs_tdf_gc.name = cs_tdf_points.name
WHERE EXTRACT(YEAR from cs_tdf_mountains.timestamp) = 2013 AND EXTRACT(YEAR from cs_tdf_gc.timestamp) = 2013 AND EXTRACT(YEAR from cs_tdf_points.timestamp) = 2013;