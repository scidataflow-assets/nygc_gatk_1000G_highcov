.PHONY: all

20190425_NYGC_GATK_manifest.txt:
	wget http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000G_2504_high_coverage/working/20190425_NYGC_GATK/20190425_NYGC_GATK_manifest.txt

../data_manifest.yml: 20190425_NYGC_GATK_manifest.txt
	(cd .. && sdf init)
	python map_manifest.py $<

all: ../data_manifest.yml
