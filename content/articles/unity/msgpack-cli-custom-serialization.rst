=============================================================
msgpack-cliでcustom serializationをする
=============================================================
:date: 2017-09-13
:tags: Unity, Android, iOS, msgpack

何かEnumをSerializeするときにErrorが起きたので以下のように対応した.

これが正しい対応かどうかはかなり怪しいが一旦はこれで対応していく.

以下を参照し、作成した.

https://github.com/msgpack/msgpack-cli/wiki/Custom-serialization       

1. CustomSerializationを作る

.. code-block:: c#

    public class TargetTypeSerializer : MessagePackSerializer<TargetType>
    {
     
        protected TargetTypeSerializer (SerializationContext ownerContext) : base (ownerContext)
        {
        }
    
        #region implemented abstract members of MessagePackSerializer
    
        protected override void PackToCore (MsgPack.Packer packer, TargetType objectTree)
        {
            packer.Pack ((int)objectTree);
        }
    
        protected override TargetType UnpackFromCore (MsgPack.Unpacker unpacker)
        {
            var data = unpacker.LastReadData;
            return (TargetType)data.AsInt16 ();
        }
    
        #endregion
        
    }

2. どっかでResolveSerilizerを登録し、setSerializerをする

.. code-block:: c#
    
   SerializationContext.Default.ResolveSerializer += (object sender, ResolveSerializerEventArgs e) => {
        if (e.TargetType == typeof(TargetType))
            e.SetSerializer (new TargetTypeSerializer (e.Context));
    };


