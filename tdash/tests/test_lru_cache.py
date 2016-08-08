"""
test for lru cache

run using py.test
"""

from tdash import lru_cache




class TestLRUCache:
    @classmethod
    def setup_class(cls):
        pass

    def test_stores_last_10(self):
        ten_item_example = lru_cache.LRUCache(10, mocked_provider_func)

        # set up lru
        populate = [ten_item_example[i] for i in range(10)]
        ten_item_example[4]
        ten_item_example[3]
        ten_item_example[11]
        ten_item_example[12]
        ten_item_example[13]
        ten_item_example[14]
        ten_item_example[15]
        ten_item_example[16]
        ten_item_example[17]

        assert set(ten_item_example._values.keys()) == set([3,4,9,11,12,13,14,15,16,17])

    def test_access_history_is_correct_order(self):
        ten_item_example = lru_cache.LRUCache(10, mocked_provider_func)
        order_to_go_in = [1,5,6,7,5,8,6,41,45,714,1,2,4,5,3,74]
        # set up lru
        populate = [ten_item_example[i] for i in order_to_go_in]

        sorted_access = sorted(ten_item_example._access_history,
                               key=lambda x: ten_item_example._access_history[x])
        print sorted_access, order_to_go_in[-10:]
        print ten_item_example._access_history
        assert sorted_access == order_to_go_in[-10:]

    def test_set_item(self):
        setting_storage = MockEntryFunc()


        items_to_populate = range(20)
        ten_item_example = lru_cache.LRUCache(10, mocked_provider_func, on_entry_func=setting_storage.on_entry_func)
        for i in items_to_populate:
            ten_item_example[i] = i+1

        assert set(setting_storage.storage.keys()) == set(items_to_populate)
        assert set(ten_item_example._values.keys()) == set(items_to_populate[-10:])

    def test_length(self):
        ten_item_example = lru_cache.LRUCache(10, mocked_provider_func)

        [ten_item_example[i] for i in range(5)]

        assert len(ten_item_example) == 5
        [ten_item_example[i] for i in range(15)]
        assert len(ten_item_example) == 10

    def test_exit_of_item(self):
        exit_item = MockExitFunc()
        ten_item_example = lru_cache.LRUCache(10, mocked_provider_func, on_evicted_func=exit_item.remove_item)

        items_to_read = [1,1000,3,88,99,101,102,103,45,6,7,1,5,7]
        for i in items_to_read:
            ten_item_example[i]
        # should now have 88,99,101,102,103,45,6,1,5,7
        # so exits are: [(1,1), (1000, 1000), (3,3)]
        ten_item_example[34] = 10
        ten_item_example[3] = 10
        ten_item_example[6] = 10
        # should now have 101,102,103,45,1,5,7,34,3,6
        # so exits are: [(88,88), (99, 99)]

        items_to_read2 = [66,7,88,4]
        for i in items_to_read2:
            ten_item_example[i]
        # should now have ,45,1,5,34,3,6,66,7,88,4
        #exits [(101, 101), (102,102), (103, 103)]

        print exit_item.storage
        assert set(ten_item_example._values.keys()) == {45,1,5,34,3,6,66,7,88,4}
        assert set(ten_item_example._access_history.keys()) == {45,1,5,34,3,6,66,7,88,4}
        assert ten_item_example._access_history == {45:8,1:11, 5:12, 34:14, 3:15, 6:16, 66:17, 7:18, 88:19, 4:20}
        print 'values', ten_item_example._values
        print 'access history ', ten_item_example._access_history
        assert exit_item.storage == [(1,1), (1000, 1000), (3,3), (88,88), (99, 99), (101, 101),
                                     (102,102), (103, 103)]


    def test_exit_of_items2(self):
        exit_item = MockExitFunc()
        ten_item_example = lru_cache.LRUCache(10, mocked_provider_func, on_evicted_func=exit_item.remove_item)

        # should now have 88,99,101,102,103,45,6,1,5,7
        # so exits are: [(1,1), (1000, 1000), (3,3)]
        ten_item_example[10] = 10
        ten_item_example[11] = 10
        ten_item_example[13] = 10
        ten_item_example[12] = 10
        ten_item_example[14] = 10
        ten_item_example[15] = 10
        ten_item_example[16] = 10
        ten_item_example[17] = 10
        ten_item_example[18] = 10
        ten_item_example[19] = 10
        ten_item_example[24] = 10
        ten_item_example[4] = 10
        print exit_item.storage
        assert exit_item.storage == [(10, 10), (11, 10)]
        assert ten_item_example._access_history == {13:2,12:3, 14:4, 15:5, 16:6, 17:7, 18:8, 19:9, 24:10, 4:11}
        assert ten_item_example._values == {13:10,12:10, 14:10, 15:10, 16:10, 17:10, 18:10, 19:10, 24:10, 4:10}





class MockExitFunc(object):
    def __init__(self):
        self.storage = []

    def remove_item(self, key, value):
        self.storage.append((key, value))



class MockEntryFunc(object):
    def __init__(self):
        self.storage = {}

    def on_entry_func(self, key, value):
        print key, value
        self.storage[key] = value




def mocked_provider_func(key):
    return key