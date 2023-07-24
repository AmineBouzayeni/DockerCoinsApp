require "test/unit"
require "digest"
require "net/http"

class CustomTest < Test::Unit::TestCase

    def test_gethostname
      res = Net::HTTP.get_response(URI("http://__IP__:__HASHER_TEST_PORT__"))
      assert_equal("200", res.code, 'Get hostname endpoint is working.')
    end
    def test_hash_with_random
      res = Net::HTTP.post(URI("http://__IP__:__HASHER_TEST_PORT__"), "random")
      assert_equal("200", res.code, 'Post hash endpoint is working.')
    end  
end