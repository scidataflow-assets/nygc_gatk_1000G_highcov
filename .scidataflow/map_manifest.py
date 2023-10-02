import sys
import csv
import yaml

BASE_URL = ("http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/"
            "1000G_2504_high_coverage/working/20190425_NYGC_GATK/")


def read_tsv(tsv_file):
    entries = []
    with open(tsv_file, 'r') as f:
        tsv_reader = csv.reader(f, delimiter='\t')
        for row in tsv_reader:
            filename, size, md5 = row
            if filename.endswith('vcf.gz.tbi') or filename.endswith('vcf.gz'):
                # skip checksum files
                entry = {
                    'path': filename,
                    'tracked': False,
                    'md5': md5,
                    'size': int(size),
                    'url': f'{BASE_URL}{filename}'
                }
                entries.append(entry)
    return entries


def map_manifest(yaml_file, new_entries):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    assert 'files' in data, "manifest must already be created with sdf init"
    data['files'].extend(new_entries)

    with open(yaml_file, 'w') as f:
        yaml.safe_dump(data, f)


# use the NYGC manifest to create the SciDataFlow manifest
tsv_file = sys.argv[1]
new_entries = read_tsv(tsv_file)

# create it in the root directory
yaml_file = '../data_manifest.yml'
map_manifest(yaml_file, new_entries)

