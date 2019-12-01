import gpt_2_simple as gpt2
import re
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--destination_path")
parser.add_argument("-c", "--checkpoint_dir", default="checkpoint")
parser.add_argument("-t", "--temp")
args = parser.parse_args()


sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
sentence = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
# gpt2.generate_to_file(sess,destination_path=args.destination_path, temperature=float(args.temp), prefix=args.prefix)


with open('./canterburytales_clean_final.txt', 'r') as s:
    position = 0
    source = s.read()
    # start at beginning of source text
    dst_length = 0
    while dst_length < 50000:
        dst = open(args.destination_path, 'a+')
        split_source = source[position:]
        # get closest sentence to current position in source text
        first_occuring_sentence = sentence.search(split_source)[0]
        print('first occuring sentence: ' + first_occuring_sentence)
        # use that sentence as a seed
        generation = gpt2.generate(sess, checkpoint_dir=args.checkpoint_dir, temperature=float(
            args.temp), prefix=first_occuring_sentence, return_as_list=True)[0]
        # add length of generated text to source text position
        position += len(generation)
        print('position: ' + str(position))
        dst.write(generation)
        dst.close()
        # check length of dst file
        dst_for_len = open(args.destination_path, 'r')
        dst_length = len(dst_for_len.read().split())
        print('word count' + str(dst_length))
        dst_for_len.close()
    s.close()
