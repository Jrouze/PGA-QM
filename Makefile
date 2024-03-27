.PHONY: txtclean PGA1_ghzall_80 PGA1 PGA2 PGA3 PGA1stop PGA2stop PGA3stop

PGA1:
		python3 PGA-QM.py -c $(CIRCUIT) $(SIZE) --num_gen 30 --num_mating 20 --pop 40 --parent_selec random \
		--cross_type two_points --cross_prob 0.5 --muta_type random --muta_prob 0.1 --stop_crit 0

PGA2:
		python3 PGA-QM.py -c $(CIRCUIT) $(SIZE) --num_gen 30 --num_mating 20 --pop 30 --parent_selec random \
		--cross_type two_points --cross_prob 0.5 --muta_type random --muta_prob 0.1 --stop_crit 0

PGA3:
		python3 PGA-QM.py -c $(CIRCUIT) $(SIZE) --num_gen 35 --num_mating 15 --pop 20 --parent_selec random \
		--cross_type two_points --cross_prob 0.5 --muta_type random --muta_prob 0.1 --stop_crit 0
		
PGA1stop:
		python3 PGA-QM.py -c $(CIRCUIT) $(SIZE) --num_gen 30 --num_mating 20 --pop 40 --parent_selec random \
		--cross_type two_points --cross_prob 0.5 --muta_type random --muta_prob 0.1 --stop_crit 10
		
PGA2stop:
		python3 PGA-QM.py -c $(CIRCUIT) $(SIZE) --num_gen 30 --num_mating 20 --pop 30 --parent_selec random \
		--cross_type two_points --cross_prob 0.5 --muta_type random --muta_prob 0.1 --stop_crit 10
		
PGA3stop:
		python3 PGA-QM.py -c $(CIRCUIT) $(SIZE) --num_gen 35 --num_mating 15 --pop 20 --parent_selec random \
		--cross_type two_points --cross_prob 0.5 --muta_type random --muta_prob 0.1 --stop_crit 10

txtclean:
		rm *.txt
