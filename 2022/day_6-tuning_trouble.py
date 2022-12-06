
def locate_marker(data_stream, marker_length):
    marker = marker_length
    for i in range(marker, len(data_stream)):
        data_chunk = data_stream[marker - marker_length:marker]

        if len(set(data_chunk)) == marker_length:
            print(marker)
            break

        marker += 1


if __name__ == '__main__':
    with open('data/6.txt', 'rt') as input_file:
        datastream_buffer = list(input_file.read().strip())

    locate_marker(datastream_buffer, 4)
    locate_marker(datastream_buffer, 14)
