const assert = require('assert');
const { isPalindrome } = require('./program3');

describe('Palindrome Checker', function () {
    it('should return true for palindromes', function () {
        assert.strictEqual(isPalindrome('level'), true);
        assert.strictEqual(isPalindrome('A man, a plan, a canal, Panama'), true);
    });

    it('should return false for non-palindromes', function () {
        assert.strictEqual(isPalindrome('hello'), false);
        assert.strictEqual(isPalindrome('not a palindrome'), false);
    });
});

